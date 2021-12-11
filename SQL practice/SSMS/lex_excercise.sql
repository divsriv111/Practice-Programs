----------------DAY 1-------------------------
--done
create table [BranchDetails]
(
BranchId int identity(1000,1) CONSTRAINT pk_BranchId_BranchDetails primary key,
BranchName varchar(50) CONSTRAINT uq_BranchName_BranchDetails unique not null,
District varchar(50) not null,
[State] varchar(50) not null,
Country varchar(50) not null,
BranchManagerId int CONSTRAINT fk_BranchManagerId_BranchDetails foreign key references [Credentials](CredentialId)
)
--done
create table [ChildCareerPolicies]
(
QuoteId int CONSTRAINT pk_QuoteId_ChildCareerPolicies primary key,
InsuredId int not null,
BeneficiaryName varchar(50) not null,
BeneficiaryDOB date not null,
PremiumMode varchar(20) not null,
RebateMode varchar(20) not null,
SumAssured money not null,
Term numeric(18) not null,
PremiumAmount money not null,
PercentageRebate decimal(18,2) not null,
PremiumModeBasedRebate money not null,
TermEndBasedRebate money not null,
TotalAmount money not null,
EffectiveDate date not null, 
ExpiryDate date not null,
NomineeName varchar(50) not null,
NomineeRelation varchar(10) not null,
BranchId int not null CONSTRAINT fk_BranchId_ChildCareerPolicies foreign key references [BranchDetails](BranchId),
ClaimsTaken int constraint df_ClaimsTaken_ChildCareerPolicies default 0,
[Status] int constraint df_Status_ChildCareerPolicies default 0,
[Comment] varchar(100) constraint df_Comment_ChildCareerPolicies default NULL
)
--done
create table Policies
(
PolicyId int identity(1,1) CONSTRAINT pk_PolicyId_Policies primary key,
PolicyType varchar(50) CONSTRAINT uq_PolicyType_Policies UNIQUE
)
--done
create table PolicyCategories
(
PolicyType varchar(50) CONSTRAINT fk_PolicyType_PolicyCategories foreign key references Policies(PolicyType),
PolicyCategoryId varchar(10) CONSTRAINT uq_PolicyCategoryId_PolicyCategories UNIQUE,
constraint cpk_PolicyCategories primary key(PolicyType,PolicyCategoryId),
PolicyCategoryName varchar(50),
[Description] varchar(100),
IsActive bit constraint chk_IsActive_PolicyCategories check(IsActive in (0,1))
)
--done
create table PolicyStatus
(
ApprovalId int CONSTRAINT pk_ApprovalId_PolicyStatus primary key,
QuoteId int not null,
CustId int not null CONSTRAINT fk_CustId_PolicyStatus foreign key references Customers(CustId),
BranchId int not null CONSTRAINT fk_BranchId_PolicyStatus foreign key references BranchDetails(BranchId),
[Status] varchar(8) constraint chk_Status_PolicyStatus check([Status] in ('Approved','Rejected','Paid')),
[Comment] varchar(200)
)
--done
create table Roles
(
RoleId INT IDENTITY(1,1) CONSTRAINT pk_RoleId_Roles primary key,
RoleName VARCHAR(50) UNIQUE NOT NULL
)
--done
create table Customers
(
CustId int identity(1000,1) CONSTRAINT pk_CustId_Customers primary key,
Gender char(1) not null,
PhoneNumber numeric(10) not null,
AddressLine1 varchar(50) not null,
City varchar(50) not null,
[State] varchar(50) not null,
Country varchar(50) not null,
PinNumber bigint not null,
[CredentialId] int CONSTRAINT fk_CredentialId_Customers foreign key references [Credentials]([CredentialId]),
FirstName varchar(20),
LastName varchar(20)
)
--done
create table [Credentials]
(
[CredentialId] INT IDENTITY(1,1) CONSTRAINT pk_CredentialId_Credentials primary key,
UserName VARCHAR(20) not null,
UserPassword VARCHAR(20), Constraint chk_UserPassword_Credentials Check(UserPassword<>Username),
RoleId int CONSTRAINT fk_RoleId_Credentials foreign key references [Roles](RoleId),
EmailId varchar(50)
)
--done
create table TransactionDetails
(
TransactionId int identity(1,1) CONSTRAINT pk_TransactionId_TransactionDetails primary key,
CustId int CONSTRAINT fk_CustId_TransactionDetails foreign key references Customers([CustId]),
QuoteId int not null,
[TransactionDate] date not null constraint df_TransactionDate_TransactionDetails default getdate(), 
[TransactionTime] time not null constraint df_TransactionTime_TransactionDetails default SYSDATETIME(), 
Amount money not null
)
GO
---------------DAY 2----------------------------
create proc usp_Register
(
@UserName VARCHAR(20),
@UserPassword VARCHAR(20),
@EmailId VARCHAR(50),
@Gender CHAR,
@PhoneNumber NUMERIC(10),
@AddressLine1 VARCHAR(50),
@City VARCHAR(50),
@State VARCHAR(50),
@Country VARCHAR(50),
@PinNumber BIGINT,
@FirstName VARCHAR(20),
@LastName VARCHAR(20)
)
AS
BEGIN
BEGIN TRY
		if @UserName = null
		begin
			return -1
		end
		if @UserPassword = null
			begin
				return -2
			end
		if @EmailId = null
			begin
				return -3
			end
		if @Gender = null
			begin
				return -4
			end
		if @PhoneNumber = null
			begin
				return -5
			end
		if @AddressLine1 = null
			begin
				return -6
			end
		if @City = null
			begin
				return -7
			end
		if @State = null
			begin
				return -8
			end
		if @Country = null
			begin
				return -9
			end
		if @PinNumber = null
			begin
				return -10
			end
		if @FirstName = null
			begin
				return -11
			end
		if @LastName = null
			begin
				return -12
			end
		insert into [Credentials](UserName,UserPassword,EmailId) values (@UserName,@UserPassword,@EmailId)
		insert into Customers(Gender,PhoneNumber,AddressLine1,City,[State],Country,PinNumber,FirstName,LastName) values
		(@Gender,@PhoneNumber,@AddressLine1,@City,@State,@Country,@PinNumber,@FirstName,@LastName)
		return 1
END TRY
BEGIN CATCH
	return -99
END CATCH
END
GO

create proc usp_UpdateCustomerDetails
(
@CustId INT,
@FirstName VARCHAR(50),
@LastName VARCHAR(50),
@ContactNumber NUMERIC(10),
@AddressLine1 VARCHAR(50),
@City VARCHAR(50),
@State VARCHAR(50),
@Country VARCHAR(50),
@PinNumber BIGINT
)
AS 
BEGIN
	begin try
			if LEN(cast(@PinNumber as VARCHAR(50))) <> 6
		BEGIN
			return -1
		END
		if @CustId = NULL 
		BEGIN
			return -2
		END
		if @FirstName = NULL
		BEGIN
			return -3
		END
		if @LastName = NULL
		BEGIN
			return -4
		END
		if @ContactNumber = NULL
		BEGIN
			return -5
		END
		if @AddressLine1 = NULL
		BEGIN
			return -6
		END
		if @City = NULL
		BEGIN
			return -7
		END
		if @State = NULL
		BEGIN
			return -8
		END
		if @Country = NULL
		BEGIN
			return -9
		END
		if @PinNumber = NULL
		BEGIN
			return -10
		END
		update Customers set FirstName=@FirstName, LastName=@LastName, PhoneNumber=@ContactNumber, AddressLine1 = @AddressLine1, City=@City,
		[State]=@State,
		Country=@Country,
		PinNumber=@PinNumber
		where CustId=@CustId
		return 1
	end try
	begin catch
		return -99
	end catch
END
GO

---------------DAY 3---------------------------
create function ufn_CheckExistenceOfUserName(@UserName Varchar(20))
returns INT
BEGIN
	if exists(select * from Credentials where UserName=@UserName)
	BEGIN
		return 1
	END
	return 0
END
GO

create function ufn_SelectAllLifeInsurancePolicies()
returns table
return (select PolicyCategoryId,PolicyCategoryName,[Description] from PolicyCategories where IsActive=1)
GO

create function ufn_GetCustomerDetails(@CredentialId int)
returns table
return (select  CustId as CustomerId, FirstName, LastName, PhoneNumber, City,[State] from Customers where CustId=@CredentialId )
GO