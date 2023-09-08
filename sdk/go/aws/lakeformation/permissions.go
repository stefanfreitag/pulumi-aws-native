// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lakeformation

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::LakeFormation::Permissions
//
// Deprecated: Permissions is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Permissions struct {
	pulumi.CustomResourceState

	DataLakePrincipal          PermissionsDataLakePrincipalOutput `pulumi:"dataLakePrincipal"`
	Permissions                pulumi.StringArrayOutput           `pulumi:"permissions"`
	PermissionsWithGrantOption pulumi.StringArrayOutput           `pulumi:"permissionsWithGrantOption"`
	Resource                   PermissionsResourceOutput          `pulumi:"resource"`
}

// NewPermissions registers a new resource with the given unique name, arguments, and options.
func NewPermissions(ctx *pulumi.Context,
	name string, args *PermissionsArgs, opts ...pulumi.ResourceOption) (*Permissions, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DataLakePrincipal == nil {
		return nil, errors.New("invalid value for required argument 'DataLakePrincipal'")
	}
	if args.Resource == nil {
		return nil, errors.New("invalid value for required argument 'Resource'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"dataLakePrincipal",
		"resource",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Permissions
	err := ctx.RegisterResource("aws-native:lakeformation:Permissions", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPermissions gets an existing Permissions resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPermissions(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PermissionsState, opts ...pulumi.ResourceOption) (*Permissions, error) {
	var resource Permissions
	err := ctx.ReadResource("aws-native:lakeformation:Permissions", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Permissions resources.
type permissionsState struct {
}

type PermissionsState struct {
}

func (PermissionsState) ElementType() reflect.Type {
	return reflect.TypeOf((*permissionsState)(nil)).Elem()
}

type permissionsArgs struct {
	DataLakePrincipal          PermissionsDataLakePrincipal `pulumi:"dataLakePrincipal"`
	Permissions                []string                     `pulumi:"permissions"`
	PermissionsWithGrantOption []string                     `pulumi:"permissionsWithGrantOption"`
	Resource                   PermissionsResource          `pulumi:"resource"`
}

// The set of arguments for constructing a Permissions resource.
type PermissionsArgs struct {
	DataLakePrincipal          PermissionsDataLakePrincipalInput
	Permissions                pulumi.StringArrayInput
	PermissionsWithGrantOption pulumi.StringArrayInput
	Resource                   PermissionsResourceInput
}

func (PermissionsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*permissionsArgs)(nil)).Elem()
}

type PermissionsInput interface {
	pulumi.Input

	ToPermissionsOutput() PermissionsOutput
	ToPermissionsOutputWithContext(ctx context.Context) PermissionsOutput
}

func (*Permissions) ElementType() reflect.Type {
	return reflect.TypeOf((**Permissions)(nil)).Elem()
}

func (i *Permissions) ToPermissionsOutput() PermissionsOutput {
	return i.ToPermissionsOutputWithContext(context.Background())
}

func (i *Permissions) ToPermissionsOutputWithContext(ctx context.Context) PermissionsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PermissionsOutput)
}

func (i *Permissions) ToOutput(ctx context.Context) pulumix.Output[*Permissions] {
	return pulumix.Output[*Permissions]{
		OutputState: i.ToPermissionsOutputWithContext(ctx).OutputState,
	}
}

type PermissionsOutput struct{ *pulumi.OutputState }

func (PermissionsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Permissions)(nil)).Elem()
}

func (o PermissionsOutput) ToPermissionsOutput() PermissionsOutput {
	return o
}

func (o PermissionsOutput) ToPermissionsOutputWithContext(ctx context.Context) PermissionsOutput {
	return o
}

func (o PermissionsOutput) ToOutput(ctx context.Context) pulumix.Output[*Permissions] {
	return pulumix.Output[*Permissions]{
		OutputState: o.OutputState,
	}
}

func (o PermissionsOutput) DataLakePrincipal() PermissionsDataLakePrincipalOutput {
	return o.ApplyT(func(v *Permissions) PermissionsDataLakePrincipalOutput { return v.DataLakePrincipal }).(PermissionsDataLakePrincipalOutput)
}

func (o PermissionsOutput) Permissions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Permissions) pulumi.StringArrayOutput { return v.Permissions }).(pulumi.StringArrayOutput)
}

func (o PermissionsOutput) PermissionsWithGrantOption() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Permissions) pulumi.StringArrayOutput { return v.PermissionsWithGrantOption }).(pulumi.StringArrayOutput)
}

func (o PermissionsOutput) Resource() PermissionsResourceOutput {
	return o.ApplyT(func(v *Permissions) PermissionsResourceOutput { return v.Resource }).(PermissionsResourceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PermissionsInput)(nil)).Elem(), &Permissions{})
	pulumi.RegisterOutputType(PermissionsOutput{})
}
