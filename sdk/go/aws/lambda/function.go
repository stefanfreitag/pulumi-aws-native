// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lambda

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Lambda::Function in region
type Function struct {
	pulumi.CustomResourceState

	Architectures FunctionArchitecturesItemArrayOutput `pulumi:"architectures"`
	// Unique identifier for function resources
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The code for the function.
	Code FunctionCodeOutput `pulumi:"code"`
	// A unique Arn for CodeSigningConfig resource
	CodeSigningConfigArn pulumi.StringPtrOutput `pulumi:"codeSigningConfigArn"`
	// A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing.
	DeadLetterConfig FunctionDeadLetterConfigPtrOutput `pulumi:"deadLetterConfig"`
	// A description of the function.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Environment variables that are accessible from function code during execution.
	Environment FunctionEnvironmentPtrOutput `pulumi:"environment"`
	// A function's ephemeral storage settings.
	EphemeralStorage FunctionEphemeralStoragePtrOutput `pulumi:"ephemeralStorage"`
	// Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget resource, you must also specify a DependsOn attribute to ensure that the mount target is created or updated before the function.
	FileSystemConfigs FunctionFileSystemConfigArrayOutput `pulumi:"fileSystemConfigs"`
	// The name of the Lambda function, up to 64 characters in length. If you don't specify a name, AWS CloudFormation generates one.
	FunctionName pulumi.StringPtrOutput `pulumi:"functionName"`
	// The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime
	Handler pulumi.StringPtrOutput `pulumi:"handler"`
	// ImageConfig
	ImageConfig FunctionImageConfigPtrOutput `pulumi:"imageConfig"`
	// The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
	KmsKeyArn pulumi.StringPtrOutput `pulumi:"kmsKeyArn"`
	// A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.
	Layers pulumi.StringArrayOutput `pulumi:"layers"`
	// The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.
	MemorySize pulumi.IntPtrOutput `pulumi:"memorySize"`
	// PackageType.
	PackageType FunctionPackageTypePtrOutput `pulumi:"packageType"`
	// The number of simultaneous executions to reserve for the function.
	ReservedConcurrentExecutions pulumi.IntPtrOutput `pulumi:"reservedConcurrentExecutions"`
	// The Amazon Resource Name (ARN) of the function's execution role.
	Role pulumi.StringOutput `pulumi:"role"`
	// The identifier of the function's runtime.
	Runtime pulumi.StringPtrOutput `pulumi:"runtime"`
	// RuntimeManagementConfig
	RuntimeManagementConfig FunctionRuntimeManagementConfigPtrOutput `pulumi:"runtimeManagementConfig"`
	// The SnapStart setting of your function
	SnapStart FunctionSnapStartPtrOutput `pulumi:"snapStart"`
	// The SnapStart response of your function
	SnapStartResponse FunctionSnapStartResponseOutput `pulumi:"snapStartResponse"`
	// A list of tags to apply to the function.
	Tags FunctionTagArrayOutput `pulumi:"tags"`
	// The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.
	Timeout pulumi.IntPtrOutput `pulumi:"timeout"`
	// Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
	TracingConfig FunctionTracingConfigPtrOutput `pulumi:"tracingConfig"`
	// For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC.
	VpcConfig FunctionVpcConfigPtrOutput `pulumi:"vpcConfig"`
}

// NewFunction registers a new resource with the given unique name, arguments, and options.
func NewFunction(ctx *pulumi.Context,
	name string, args *FunctionArgs, opts ...pulumi.ResourceOption) (*Function, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Code == nil {
		return nil, errors.New("invalid value for required argument 'Code'")
	}
	if args.Role == nil {
		return nil, errors.New("invalid value for required argument 'Role'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"functionName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Function
	err := ctx.RegisterResource("aws-native:lambda:Function", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFunction gets an existing Function resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFunction(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FunctionState, opts ...pulumi.ResourceOption) (*Function, error) {
	var resource Function
	err := ctx.ReadResource("aws-native:lambda:Function", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Function resources.
type functionState struct {
}

type FunctionState struct {
}

func (FunctionState) ElementType() reflect.Type {
	return reflect.TypeOf((*functionState)(nil)).Elem()
}

type functionArgs struct {
	Architectures []FunctionArchitecturesItem `pulumi:"architectures"`
	// The code for the function.
	Code FunctionCode `pulumi:"code"`
	// A unique Arn for CodeSigningConfig resource
	CodeSigningConfigArn *string `pulumi:"codeSigningConfigArn"`
	// A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing.
	DeadLetterConfig *FunctionDeadLetterConfig `pulumi:"deadLetterConfig"`
	// A description of the function.
	Description *string `pulumi:"description"`
	// Environment variables that are accessible from function code during execution.
	Environment *FunctionEnvironment `pulumi:"environment"`
	// A function's ephemeral storage settings.
	EphemeralStorage *FunctionEphemeralStorage `pulumi:"ephemeralStorage"`
	// Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget resource, you must also specify a DependsOn attribute to ensure that the mount target is created or updated before the function.
	FileSystemConfigs []FunctionFileSystemConfig `pulumi:"fileSystemConfigs"`
	// The name of the Lambda function, up to 64 characters in length. If you don't specify a name, AWS CloudFormation generates one.
	FunctionName *string `pulumi:"functionName"`
	// The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime
	Handler *string `pulumi:"handler"`
	// ImageConfig
	ImageConfig *FunctionImageConfig `pulumi:"imageConfig"`
	// The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
	KmsKeyArn *string `pulumi:"kmsKeyArn"`
	// A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.
	Layers []string `pulumi:"layers"`
	// The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.
	MemorySize *int `pulumi:"memorySize"`
	// PackageType.
	PackageType *FunctionPackageType `pulumi:"packageType"`
	// The number of simultaneous executions to reserve for the function.
	ReservedConcurrentExecutions *int `pulumi:"reservedConcurrentExecutions"`
	// The Amazon Resource Name (ARN) of the function's execution role.
	Role string `pulumi:"role"`
	// The identifier of the function's runtime.
	Runtime *string `pulumi:"runtime"`
	// RuntimeManagementConfig
	RuntimeManagementConfig *FunctionRuntimeManagementConfig `pulumi:"runtimeManagementConfig"`
	// The SnapStart setting of your function
	SnapStart *FunctionSnapStart `pulumi:"snapStart"`
	// A list of tags to apply to the function.
	Tags []FunctionTag `pulumi:"tags"`
	// The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.
	Timeout *int `pulumi:"timeout"`
	// Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
	TracingConfig *FunctionTracingConfig `pulumi:"tracingConfig"`
	// For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC.
	VpcConfig *FunctionVpcConfig `pulumi:"vpcConfig"`
}

// The set of arguments for constructing a Function resource.
type FunctionArgs struct {
	Architectures FunctionArchitecturesItemArrayInput
	// The code for the function.
	Code FunctionCodeInput
	// A unique Arn for CodeSigningConfig resource
	CodeSigningConfigArn pulumi.StringPtrInput
	// A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing.
	DeadLetterConfig FunctionDeadLetterConfigPtrInput
	// A description of the function.
	Description pulumi.StringPtrInput
	// Environment variables that are accessible from function code during execution.
	Environment FunctionEnvironmentPtrInput
	// A function's ephemeral storage settings.
	EphemeralStorage FunctionEphemeralStoragePtrInput
	// Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget resource, you must also specify a DependsOn attribute to ensure that the mount target is created or updated before the function.
	FileSystemConfigs FunctionFileSystemConfigArrayInput
	// The name of the Lambda function, up to 64 characters in length. If you don't specify a name, AWS CloudFormation generates one.
	FunctionName pulumi.StringPtrInput
	// The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime
	Handler pulumi.StringPtrInput
	// ImageConfig
	ImageConfig FunctionImageConfigPtrInput
	// The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
	KmsKeyArn pulumi.StringPtrInput
	// A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.
	Layers pulumi.StringArrayInput
	// The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.
	MemorySize pulumi.IntPtrInput
	// PackageType.
	PackageType FunctionPackageTypePtrInput
	// The number of simultaneous executions to reserve for the function.
	ReservedConcurrentExecutions pulumi.IntPtrInput
	// The Amazon Resource Name (ARN) of the function's execution role.
	Role pulumi.StringInput
	// The identifier of the function's runtime.
	Runtime pulumi.StringPtrInput
	// RuntimeManagementConfig
	RuntimeManagementConfig FunctionRuntimeManagementConfigPtrInput
	// The SnapStart setting of your function
	SnapStart FunctionSnapStartPtrInput
	// A list of tags to apply to the function.
	Tags FunctionTagArrayInput
	// The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.
	Timeout pulumi.IntPtrInput
	// Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
	TracingConfig FunctionTracingConfigPtrInput
	// For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC.
	VpcConfig FunctionVpcConfigPtrInput
}

func (FunctionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*functionArgs)(nil)).Elem()
}

type FunctionInput interface {
	pulumi.Input

	ToFunctionOutput() FunctionOutput
	ToFunctionOutputWithContext(ctx context.Context) FunctionOutput
}

func (*Function) ElementType() reflect.Type {
	return reflect.TypeOf((**Function)(nil)).Elem()
}

func (i *Function) ToFunctionOutput() FunctionOutput {
	return i.ToFunctionOutputWithContext(context.Background())
}

func (i *Function) ToFunctionOutputWithContext(ctx context.Context) FunctionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FunctionOutput)
}

func (i *Function) ToOutput(ctx context.Context) pulumix.Output[*Function] {
	return pulumix.Output[*Function]{
		OutputState: i.ToFunctionOutputWithContext(ctx).OutputState,
	}
}

type FunctionOutput struct{ *pulumi.OutputState }

func (FunctionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Function)(nil)).Elem()
}

func (o FunctionOutput) ToFunctionOutput() FunctionOutput {
	return o
}

func (o FunctionOutput) ToFunctionOutputWithContext(ctx context.Context) FunctionOutput {
	return o
}

func (o FunctionOutput) ToOutput(ctx context.Context) pulumix.Output[*Function] {
	return pulumix.Output[*Function]{
		OutputState: o.OutputState,
	}
}

func (o FunctionOutput) Architectures() FunctionArchitecturesItemArrayOutput {
	return o.ApplyT(func(v *Function) FunctionArchitecturesItemArrayOutput { return v.Architectures }).(FunctionArchitecturesItemArrayOutput)
}

// Unique identifier for function resources
func (o FunctionOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Function) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The code for the function.
func (o FunctionOutput) Code() FunctionCodeOutput {
	return o.ApplyT(func(v *Function) FunctionCodeOutput { return v.Code }).(FunctionCodeOutput)
}

// A unique Arn for CodeSigningConfig resource
func (o FunctionOutput) CodeSigningConfigArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Function) pulumi.StringPtrOutput { return v.CodeSigningConfigArn }).(pulumi.StringPtrOutput)
}

// A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing.
func (o FunctionOutput) DeadLetterConfig() FunctionDeadLetterConfigPtrOutput {
	return o.ApplyT(func(v *Function) FunctionDeadLetterConfigPtrOutput { return v.DeadLetterConfig }).(FunctionDeadLetterConfigPtrOutput)
}

// A description of the function.
func (o FunctionOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Function) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Environment variables that are accessible from function code during execution.
func (o FunctionOutput) Environment() FunctionEnvironmentPtrOutput {
	return o.ApplyT(func(v *Function) FunctionEnvironmentPtrOutput { return v.Environment }).(FunctionEnvironmentPtrOutput)
}

// A function's ephemeral storage settings.
func (o FunctionOutput) EphemeralStorage() FunctionEphemeralStoragePtrOutput {
	return o.ApplyT(func(v *Function) FunctionEphemeralStoragePtrOutput { return v.EphemeralStorage }).(FunctionEphemeralStoragePtrOutput)
}

// Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget resource, you must also specify a DependsOn attribute to ensure that the mount target is created or updated before the function.
func (o FunctionOutput) FileSystemConfigs() FunctionFileSystemConfigArrayOutput {
	return o.ApplyT(func(v *Function) FunctionFileSystemConfigArrayOutput { return v.FileSystemConfigs }).(FunctionFileSystemConfigArrayOutput)
}

// The name of the Lambda function, up to 64 characters in length. If you don't specify a name, AWS CloudFormation generates one.
func (o FunctionOutput) FunctionName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Function) pulumi.StringPtrOutput { return v.FunctionName }).(pulumi.StringPtrOutput)
}

// The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime
func (o FunctionOutput) Handler() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Function) pulumi.StringPtrOutput { return v.Handler }).(pulumi.StringPtrOutput)
}

// ImageConfig
func (o FunctionOutput) ImageConfig() FunctionImageConfigPtrOutput {
	return o.ApplyT(func(v *Function) FunctionImageConfigPtrOutput { return v.ImageConfig }).(FunctionImageConfigPtrOutput)
}

// The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
func (o FunctionOutput) KmsKeyArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Function) pulumi.StringPtrOutput { return v.KmsKeyArn }).(pulumi.StringPtrOutput)
}

// A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.
func (o FunctionOutput) Layers() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Function) pulumi.StringArrayOutput { return v.Layers }).(pulumi.StringArrayOutput)
}

// The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.
func (o FunctionOutput) MemorySize() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Function) pulumi.IntPtrOutput { return v.MemorySize }).(pulumi.IntPtrOutput)
}

// PackageType.
func (o FunctionOutput) PackageType() FunctionPackageTypePtrOutput {
	return o.ApplyT(func(v *Function) FunctionPackageTypePtrOutput { return v.PackageType }).(FunctionPackageTypePtrOutput)
}

// The number of simultaneous executions to reserve for the function.
func (o FunctionOutput) ReservedConcurrentExecutions() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Function) pulumi.IntPtrOutput { return v.ReservedConcurrentExecutions }).(pulumi.IntPtrOutput)
}

// The Amazon Resource Name (ARN) of the function's execution role.
func (o FunctionOutput) Role() pulumi.StringOutput {
	return o.ApplyT(func(v *Function) pulumi.StringOutput { return v.Role }).(pulumi.StringOutput)
}

// The identifier of the function's runtime.
func (o FunctionOutput) Runtime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Function) pulumi.StringPtrOutput { return v.Runtime }).(pulumi.StringPtrOutput)
}

// RuntimeManagementConfig
func (o FunctionOutput) RuntimeManagementConfig() FunctionRuntimeManagementConfigPtrOutput {
	return o.ApplyT(func(v *Function) FunctionRuntimeManagementConfigPtrOutput { return v.RuntimeManagementConfig }).(FunctionRuntimeManagementConfigPtrOutput)
}

// The SnapStart setting of your function
func (o FunctionOutput) SnapStart() FunctionSnapStartPtrOutput {
	return o.ApplyT(func(v *Function) FunctionSnapStartPtrOutput { return v.SnapStart }).(FunctionSnapStartPtrOutput)
}

// The SnapStart response of your function
func (o FunctionOutput) SnapStartResponse() FunctionSnapStartResponseOutput {
	return o.ApplyT(func(v *Function) FunctionSnapStartResponseOutput { return v.SnapStartResponse }).(FunctionSnapStartResponseOutput)
}

// A list of tags to apply to the function.
func (o FunctionOutput) Tags() FunctionTagArrayOutput {
	return o.ApplyT(func(v *Function) FunctionTagArrayOutput { return v.Tags }).(FunctionTagArrayOutput)
}

// The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.
func (o FunctionOutput) Timeout() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Function) pulumi.IntPtrOutput { return v.Timeout }).(pulumi.IntPtrOutput)
}

// Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
func (o FunctionOutput) TracingConfig() FunctionTracingConfigPtrOutput {
	return o.ApplyT(func(v *Function) FunctionTracingConfigPtrOutput { return v.TracingConfig }).(FunctionTracingConfigPtrOutput)
}

// For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC.
func (o FunctionOutput) VpcConfig() FunctionVpcConfigPtrOutput {
	return o.ApplyT(func(v *Function) FunctionVpcConfigPtrOutput { return v.VpcConfig }).(FunctionVpcConfigPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FunctionInput)(nil)).Elem(), &Function{})
	pulumi.RegisterOutputType(FunctionOutput{})
}
