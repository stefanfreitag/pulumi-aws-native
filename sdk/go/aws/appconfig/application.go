// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appconfig

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::AppConfig::Application
//
// Deprecated: Application is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Application struct {
	pulumi.CustomResourceState

	Description pulumi.StringPtrOutput     `pulumi:"description"`
	Name        pulumi.StringOutput        `pulumi:"name"`
	Tags        ApplicationTagsArrayOutput `pulumi:"tags"`
}

// NewApplication registers a new resource with the given unique name, arguments, and options.
func NewApplication(ctx *pulumi.Context,
	name string, args *ApplicationArgs, opts ...pulumi.ResourceOption) (*Application, error) {
	if args == nil {
		args = &ApplicationArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Application
	err := ctx.RegisterResource("aws-native:appconfig:Application", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetApplication gets an existing Application resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApplication(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ApplicationState, opts ...pulumi.ResourceOption) (*Application, error) {
	var resource Application
	err := ctx.ReadResource("aws-native:appconfig:Application", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Application resources.
type applicationState struct {
}

type ApplicationState struct {
}

func (ApplicationState) ElementType() reflect.Type {
	return reflect.TypeOf((*applicationState)(nil)).Elem()
}

type applicationArgs struct {
	Description *string           `pulumi:"description"`
	Name        *string           `pulumi:"name"`
	Tags        []ApplicationTags `pulumi:"tags"`
}

// The set of arguments for constructing a Application resource.
type ApplicationArgs struct {
	Description pulumi.StringPtrInput
	Name        pulumi.StringPtrInput
	Tags        ApplicationTagsArrayInput
}

func (ApplicationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*applicationArgs)(nil)).Elem()
}

type ApplicationInput interface {
	pulumi.Input

	ToApplicationOutput() ApplicationOutput
	ToApplicationOutputWithContext(ctx context.Context) ApplicationOutput
}

func (*Application) ElementType() reflect.Type {
	return reflect.TypeOf((**Application)(nil)).Elem()
}

func (i *Application) ToApplicationOutput() ApplicationOutput {
	return i.ToApplicationOutputWithContext(context.Background())
}

func (i *Application) ToApplicationOutputWithContext(ctx context.Context) ApplicationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ApplicationOutput)
}

func (i *Application) ToOutput(ctx context.Context) pulumix.Output[*Application] {
	return pulumix.Output[*Application]{
		OutputState: i.ToApplicationOutputWithContext(ctx).OutputState,
	}
}

type ApplicationOutput struct{ *pulumi.OutputState }

func (ApplicationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Application)(nil)).Elem()
}

func (o ApplicationOutput) ToApplicationOutput() ApplicationOutput {
	return o
}

func (o ApplicationOutput) ToApplicationOutputWithContext(ctx context.Context) ApplicationOutput {
	return o
}

func (o ApplicationOutput) ToOutput(ctx context.Context) pulumix.Output[*Application] {
	return pulumix.Output[*Application]{
		OutputState: o.OutputState,
	}
}

func (o ApplicationOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Application) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o ApplicationOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Application) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o ApplicationOutput) Tags() ApplicationTagsArrayOutput {
	return o.ApplyT(func(v *Application) ApplicationTagsArrayOutput { return v.Tags }).(ApplicationTagsArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ApplicationInput)(nil)).Elem(), &Application{})
	pulumi.RegisterOutputType(ApplicationOutput{})
}
