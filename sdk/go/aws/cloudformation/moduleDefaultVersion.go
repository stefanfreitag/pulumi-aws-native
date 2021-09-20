// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudformation

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A module that has been registered in the CloudFormation registry as the default version
type ModuleDefaultVersion struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the module version to set as the default version.
	Arn pulumi.StringPtrOutput `pulumi:"arn"`
	// The name of a module existing in the registry.
	ModuleName pulumi.StringPtrOutput `pulumi:"moduleName"`
	// The ID of an existing version of the named module to set as the default.
	VersionId pulumi.StringPtrOutput `pulumi:"versionId"`
}

// NewModuleDefaultVersion registers a new resource with the given unique name, arguments, and options.
func NewModuleDefaultVersion(ctx *pulumi.Context,
	name string, args *ModuleDefaultVersionArgs, opts ...pulumi.ResourceOption) (*ModuleDefaultVersion, error) {
	if args == nil {
		args = &ModuleDefaultVersionArgs{}
	}

	var resource ModuleDefaultVersion
	err := ctx.RegisterResource("aws-native:cloudformation:ModuleDefaultVersion", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetModuleDefaultVersion gets an existing ModuleDefaultVersion resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetModuleDefaultVersion(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ModuleDefaultVersionState, opts ...pulumi.ResourceOption) (*ModuleDefaultVersion, error) {
	var resource ModuleDefaultVersion
	err := ctx.ReadResource("aws-native:cloudformation:ModuleDefaultVersion", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ModuleDefaultVersion resources.
type moduleDefaultVersionState struct {
}

type ModuleDefaultVersionState struct {
}

func (ModuleDefaultVersionState) ElementType() reflect.Type {
	return reflect.TypeOf((*moduleDefaultVersionState)(nil)).Elem()
}

type moduleDefaultVersionArgs struct {
	// The Amazon Resource Name (ARN) of the module version to set as the default version.
	Arn *string `pulumi:"arn"`
	// The name of a module existing in the registry.
	ModuleName *string `pulumi:"moduleName"`
	// The ID of an existing version of the named module to set as the default.
	VersionId *string `pulumi:"versionId"`
}

// The set of arguments for constructing a ModuleDefaultVersion resource.
type ModuleDefaultVersionArgs struct {
	// The Amazon Resource Name (ARN) of the module version to set as the default version.
	Arn pulumi.StringPtrInput
	// The name of a module existing in the registry.
	ModuleName pulumi.StringPtrInput
	// The ID of an existing version of the named module to set as the default.
	VersionId pulumi.StringPtrInput
}

func (ModuleDefaultVersionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*moduleDefaultVersionArgs)(nil)).Elem()
}

type ModuleDefaultVersionInput interface {
	pulumi.Input

	ToModuleDefaultVersionOutput() ModuleDefaultVersionOutput
	ToModuleDefaultVersionOutputWithContext(ctx context.Context) ModuleDefaultVersionOutput
}

func (*ModuleDefaultVersion) ElementType() reflect.Type {
	return reflect.TypeOf((*ModuleDefaultVersion)(nil))
}

func (i *ModuleDefaultVersion) ToModuleDefaultVersionOutput() ModuleDefaultVersionOutput {
	return i.ToModuleDefaultVersionOutputWithContext(context.Background())
}

func (i *ModuleDefaultVersion) ToModuleDefaultVersionOutputWithContext(ctx context.Context) ModuleDefaultVersionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModuleDefaultVersionOutput)
}

type ModuleDefaultVersionOutput struct{ *pulumi.OutputState }

func (ModuleDefaultVersionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ModuleDefaultVersion)(nil))
}

func (o ModuleDefaultVersionOutput) ToModuleDefaultVersionOutput() ModuleDefaultVersionOutput {
	return o
}

func (o ModuleDefaultVersionOutput) ToModuleDefaultVersionOutputWithContext(ctx context.Context) ModuleDefaultVersionOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ModuleDefaultVersionOutput{})
}
