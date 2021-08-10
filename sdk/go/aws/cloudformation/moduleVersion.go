// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudformation

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html
type ModuleVersion struct {
	pulumi.CustomResourceState

	Arn              pulumi.StringOutput `pulumi:"arn"`
	Description      pulumi.StringOutput `pulumi:"description"`
	DocumentationUrl pulumi.StringOutput `pulumi:"documentationUrl"`
	IsDefaultVersion pulumi.BoolOutput   `pulumi:"isDefaultVersion"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulename
	ModuleName pulumi.StringOutput `pulumi:"moduleName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulepackage
	ModulePackage pulumi.StringPtrOutput `pulumi:"modulePackage"`
	Schema        pulumi.StringOutput    `pulumi:"schema"`
	TimeCreated   pulumi.StringOutput    `pulumi:"timeCreated"`
	VersionId     pulumi.StringOutput    `pulumi:"versionId"`
	Visibility    pulumi.StringOutput    `pulumi:"visibility"`
}

// NewModuleVersion registers a new resource with the given unique name, arguments, and options.
func NewModuleVersion(ctx *pulumi.Context,
	name string, args *ModuleVersionArgs, opts ...pulumi.ResourceOption) (*ModuleVersion, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ModuleName == nil {
		return nil, errors.New("invalid value for required argument 'ModuleName'")
	}
	var resource ModuleVersion
	err := ctx.RegisterResource("aws-native:CloudFormation:ModuleVersion", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetModuleVersion gets an existing ModuleVersion resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetModuleVersion(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ModuleVersionState, opts ...pulumi.ResourceOption) (*ModuleVersion, error) {
	var resource ModuleVersion
	err := ctx.ReadResource("aws-native:CloudFormation:ModuleVersion", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ModuleVersion resources.
type moduleVersionState struct {
}

type ModuleVersionState struct {
}

func (ModuleVersionState) ElementType() reflect.Type {
	return reflect.TypeOf((*moduleVersionState)(nil)).Elem()
}

type moduleVersionArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulename
	ModuleName string `pulumi:"moduleName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulepackage
	ModulePackage *string `pulumi:"modulePackage"`
}

// The set of arguments for constructing a ModuleVersion resource.
type ModuleVersionArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulename
	ModuleName pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulepackage
	ModulePackage pulumi.StringPtrInput
}

func (ModuleVersionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*moduleVersionArgs)(nil)).Elem()
}

type ModuleVersionInput interface {
	pulumi.Input

	ToModuleVersionOutput() ModuleVersionOutput
	ToModuleVersionOutputWithContext(ctx context.Context) ModuleVersionOutput
}

func (*ModuleVersion) ElementType() reflect.Type {
	return reflect.TypeOf((*ModuleVersion)(nil))
}

func (i *ModuleVersion) ToModuleVersionOutput() ModuleVersionOutput {
	return i.ToModuleVersionOutputWithContext(context.Background())
}

func (i *ModuleVersion) ToModuleVersionOutputWithContext(ctx context.Context) ModuleVersionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModuleVersionOutput)
}

type ModuleVersionOutput struct{ *pulumi.OutputState }

func (ModuleVersionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ModuleVersion)(nil))
}

func (o ModuleVersionOutput) ToModuleVersionOutput() ModuleVersionOutput {
	return o
}

func (o ModuleVersionOutput) ToModuleVersionOutputWithContext(ctx context.Context) ModuleVersionOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ModuleVersionOutput{})
}
