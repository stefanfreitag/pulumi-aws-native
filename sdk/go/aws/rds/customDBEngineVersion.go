// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::RDS::CustomDBEngineVersion resource creates an Amazon RDS custom DB engine version.
type CustomDBEngineVersion struct {
	pulumi.CustomResourceState

	// The ARN of the custom engine version.
	DBEngineVersionArn pulumi.StringOutput `pulumi:"dBEngineVersionArn"`
	// The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.
	DatabaseInstallationFilesS3BucketName pulumi.StringOutput `pulumi:"databaseInstallationFilesS3BucketName"`
	// The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1`. If this setting isn't specified, no prefix is assumed.
	DatabaseInstallationFilesS3Prefix pulumi.StringPtrOutput `pulumi:"databaseInstallationFilesS3Prefix"`
	// An optional description of your CEV.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
	Engine pulumi.StringOutput `pulumi:"engine"`
	// The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
	EngineVersion pulumi.StringOutput `pulumi:"engineVersion"`
	// The AWS KMS key identifier for an encrypted CEV. A symmetric KMS key is required for RDS Custom, but optional for Amazon RDS.
	KMSKeyId pulumi.StringPtrOutput `pulumi:"kMSKeyId"`
	// The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.
	Manifest pulumi.StringPtrOutput `pulumi:"manifest"`
	// The availability status to be assigned to the CEV.
	Status CustomDBEngineVersionStatusPtrOutput `pulumi:"status"`
	// An array of key-value pairs to apply to this resource.
	Tags CustomDBEngineVersionTagArrayOutput `pulumi:"tags"`
}

// NewCustomDBEngineVersion registers a new resource with the given unique name, arguments, and options.
func NewCustomDBEngineVersion(ctx *pulumi.Context,
	name string, args *CustomDBEngineVersionArgs, opts ...pulumi.ResourceOption) (*CustomDBEngineVersion, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DatabaseInstallationFilesS3BucketName == nil {
		return nil, errors.New("invalid value for required argument 'DatabaseInstallationFilesS3BucketName'")
	}
	if args.Engine == nil {
		return nil, errors.New("invalid value for required argument 'Engine'")
	}
	if args.EngineVersion == nil {
		return nil, errors.New("invalid value for required argument 'EngineVersion'")
	}
	var resource CustomDBEngineVersion
	err := ctx.RegisterResource("aws-native:rds:CustomDBEngineVersion", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCustomDBEngineVersion gets an existing CustomDBEngineVersion resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCustomDBEngineVersion(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CustomDBEngineVersionState, opts ...pulumi.ResourceOption) (*CustomDBEngineVersion, error) {
	var resource CustomDBEngineVersion
	err := ctx.ReadResource("aws-native:rds:CustomDBEngineVersion", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CustomDBEngineVersion resources.
type customDBEngineVersionState struct {
}

type CustomDBEngineVersionState struct {
}

func (CustomDBEngineVersionState) ElementType() reflect.Type {
	return reflect.TypeOf((*customDBEngineVersionState)(nil)).Elem()
}

type customDBEngineVersionArgs struct {
	// The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.
	DatabaseInstallationFilesS3BucketName string `pulumi:"databaseInstallationFilesS3BucketName"`
	// The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1`. If this setting isn't specified, no prefix is assumed.
	DatabaseInstallationFilesS3Prefix *string `pulumi:"databaseInstallationFilesS3Prefix"`
	// An optional description of your CEV.
	Description *string `pulumi:"description"`
	// The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
	Engine string `pulumi:"engine"`
	// The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
	EngineVersion string `pulumi:"engineVersion"`
	// The AWS KMS key identifier for an encrypted CEV. A symmetric KMS key is required for RDS Custom, but optional for Amazon RDS.
	KMSKeyId *string `pulumi:"kMSKeyId"`
	// The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.
	Manifest *string `pulumi:"manifest"`
	// The availability status to be assigned to the CEV.
	Status *CustomDBEngineVersionStatus `pulumi:"status"`
	// An array of key-value pairs to apply to this resource.
	Tags []CustomDBEngineVersionTag `pulumi:"tags"`
}

// The set of arguments for constructing a CustomDBEngineVersion resource.
type CustomDBEngineVersionArgs struct {
	// The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.
	DatabaseInstallationFilesS3BucketName pulumi.StringInput
	// The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1`. If this setting isn't specified, no prefix is assumed.
	DatabaseInstallationFilesS3Prefix pulumi.StringPtrInput
	// An optional description of your CEV.
	Description pulumi.StringPtrInput
	// The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
	Engine pulumi.StringInput
	// The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
	EngineVersion pulumi.StringInput
	// The AWS KMS key identifier for an encrypted CEV. A symmetric KMS key is required for RDS Custom, but optional for Amazon RDS.
	KMSKeyId pulumi.StringPtrInput
	// The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.
	Manifest pulumi.StringPtrInput
	// The availability status to be assigned to the CEV.
	Status CustomDBEngineVersionStatusPtrInput
	// An array of key-value pairs to apply to this resource.
	Tags CustomDBEngineVersionTagArrayInput
}

func (CustomDBEngineVersionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*customDBEngineVersionArgs)(nil)).Elem()
}

type CustomDBEngineVersionInput interface {
	pulumi.Input

	ToCustomDBEngineVersionOutput() CustomDBEngineVersionOutput
	ToCustomDBEngineVersionOutputWithContext(ctx context.Context) CustomDBEngineVersionOutput
}

func (*CustomDBEngineVersion) ElementType() reflect.Type {
	return reflect.TypeOf((**CustomDBEngineVersion)(nil)).Elem()
}

func (i *CustomDBEngineVersion) ToCustomDBEngineVersionOutput() CustomDBEngineVersionOutput {
	return i.ToCustomDBEngineVersionOutputWithContext(context.Background())
}

func (i *CustomDBEngineVersion) ToCustomDBEngineVersionOutputWithContext(ctx context.Context) CustomDBEngineVersionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomDBEngineVersionOutput)
}

type CustomDBEngineVersionOutput struct{ *pulumi.OutputState }

func (CustomDBEngineVersionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CustomDBEngineVersion)(nil)).Elem()
}

func (o CustomDBEngineVersionOutput) ToCustomDBEngineVersionOutput() CustomDBEngineVersionOutput {
	return o
}

func (o CustomDBEngineVersionOutput) ToCustomDBEngineVersionOutputWithContext(ctx context.Context) CustomDBEngineVersionOutput {
	return o
}

// The ARN of the custom engine version.
func (o CustomDBEngineVersionOutput) DBEngineVersionArn() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDBEngineVersion) pulumi.StringOutput { return v.DBEngineVersionArn }).(pulumi.StringOutput)
}

// The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.
func (o CustomDBEngineVersionOutput) DatabaseInstallationFilesS3BucketName() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDBEngineVersion) pulumi.StringOutput { return v.DatabaseInstallationFilesS3BucketName }).(pulumi.StringOutput)
}

// The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1`. If this setting isn't specified, no prefix is assumed.
func (o CustomDBEngineVersionOutput) DatabaseInstallationFilesS3Prefix() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CustomDBEngineVersion) pulumi.StringPtrOutput { return v.DatabaseInstallationFilesS3Prefix }).(pulumi.StringPtrOutput)
}

// An optional description of your CEV.
func (o CustomDBEngineVersionOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CustomDBEngineVersion) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
func (o CustomDBEngineVersionOutput) Engine() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDBEngineVersion) pulumi.StringOutput { return v.Engine }).(pulumi.StringOutput)
}

// The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
func (o CustomDBEngineVersionOutput) EngineVersion() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDBEngineVersion) pulumi.StringOutput { return v.EngineVersion }).(pulumi.StringOutput)
}

// The AWS KMS key identifier for an encrypted CEV. A symmetric KMS key is required for RDS Custom, but optional for Amazon RDS.
func (o CustomDBEngineVersionOutput) KMSKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CustomDBEngineVersion) pulumi.StringPtrOutput { return v.KMSKeyId }).(pulumi.StringPtrOutput)
}

// The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.
func (o CustomDBEngineVersionOutput) Manifest() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CustomDBEngineVersion) pulumi.StringPtrOutput { return v.Manifest }).(pulumi.StringPtrOutput)
}

// The availability status to be assigned to the CEV.
func (o CustomDBEngineVersionOutput) Status() CustomDBEngineVersionStatusPtrOutput {
	return o.ApplyT(func(v *CustomDBEngineVersion) CustomDBEngineVersionStatusPtrOutput { return v.Status }).(CustomDBEngineVersionStatusPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o CustomDBEngineVersionOutput) Tags() CustomDBEngineVersionTagArrayOutput {
	return o.ApplyT(func(v *CustomDBEngineVersion) CustomDBEngineVersionTagArrayOutput { return v.Tags }).(CustomDBEngineVersionTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CustomDBEngineVersionInput)(nil)).Elem(), &CustomDBEngineVersion{})
	pulumi.RegisterOutputType(CustomDBEngineVersionOutput{})
}
