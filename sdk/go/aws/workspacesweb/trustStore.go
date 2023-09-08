// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package workspacesweb

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of AWS::WorkSpacesWeb::TrustStore Resource Type
type TrustStore struct {
	pulumi.CustomResourceState

	AssociatedPortalArns pulumi.StringArrayOutput `pulumi:"associatedPortalArns"`
	CertificateList      pulumi.StringArrayOutput `pulumi:"certificateList"`
	Tags                 TrustStoreTagArrayOutput `pulumi:"tags"`
	TrustStoreArn        pulumi.StringOutput      `pulumi:"trustStoreArn"`
}

// NewTrustStore registers a new resource with the given unique name, arguments, and options.
func NewTrustStore(ctx *pulumi.Context,
	name string, args *TrustStoreArgs, opts ...pulumi.ResourceOption) (*TrustStore, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CertificateList == nil {
		return nil, errors.New("invalid value for required argument 'CertificateList'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource TrustStore
	err := ctx.RegisterResource("aws-native:workspacesweb:TrustStore", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTrustStore gets an existing TrustStore resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTrustStore(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TrustStoreState, opts ...pulumi.ResourceOption) (*TrustStore, error) {
	var resource TrustStore
	err := ctx.ReadResource("aws-native:workspacesweb:TrustStore", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TrustStore resources.
type trustStoreState struct {
}

type TrustStoreState struct {
}

func (TrustStoreState) ElementType() reflect.Type {
	return reflect.TypeOf((*trustStoreState)(nil)).Elem()
}

type trustStoreArgs struct {
	CertificateList []string        `pulumi:"certificateList"`
	Tags            []TrustStoreTag `pulumi:"tags"`
}

// The set of arguments for constructing a TrustStore resource.
type TrustStoreArgs struct {
	CertificateList pulumi.StringArrayInput
	Tags            TrustStoreTagArrayInput
}

func (TrustStoreArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*trustStoreArgs)(nil)).Elem()
}

type TrustStoreInput interface {
	pulumi.Input

	ToTrustStoreOutput() TrustStoreOutput
	ToTrustStoreOutputWithContext(ctx context.Context) TrustStoreOutput
}

func (*TrustStore) ElementType() reflect.Type {
	return reflect.TypeOf((**TrustStore)(nil)).Elem()
}

func (i *TrustStore) ToTrustStoreOutput() TrustStoreOutput {
	return i.ToTrustStoreOutputWithContext(context.Background())
}

func (i *TrustStore) ToTrustStoreOutputWithContext(ctx context.Context) TrustStoreOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TrustStoreOutput)
}

func (i *TrustStore) ToOutput(ctx context.Context) pulumix.Output[*TrustStore] {
	return pulumix.Output[*TrustStore]{
		OutputState: i.ToTrustStoreOutputWithContext(ctx).OutputState,
	}
}

type TrustStoreOutput struct{ *pulumi.OutputState }

func (TrustStoreOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TrustStore)(nil)).Elem()
}

func (o TrustStoreOutput) ToTrustStoreOutput() TrustStoreOutput {
	return o
}

func (o TrustStoreOutput) ToTrustStoreOutputWithContext(ctx context.Context) TrustStoreOutput {
	return o
}

func (o TrustStoreOutput) ToOutput(ctx context.Context) pulumix.Output[*TrustStore] {
	return pulumix.Output[*TrustStore]{
		OutputState: o.OutputState,
	}
}

func (o TrustStoreOutput) AssociatedPortalArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *TrustStore) pulumi.StringArrayOutput { return v.AssociatedPortalArns }).(pulumi.StringArrayOutput)
}

func (o TrustStoreOutput) CertificateList() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *TrustStore) pulumi.StringArrayOutput { return v.CertificateList }).(pulumi.StringArrayOutput)
}

func (o TrustStoreOutput) Tags() TrustStoreTagArrayOutput {
	return o.ApplyT(func(v *TrustStore) TrustStoreTagArrayOutput { return v.Tags }).(TrustStoreTagArrayOutput)
}

func (o TrustStoreOutput) TrustStoreArn() pulumi.StringOutput {
	return o.ApplyT(func(v *TrustStore) pulumi.StringOutput { return v.TrustStoreArn }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TrustStoreInput)(nil)).Elem(), &TrustStore{})
	pulumi.RegisterOutputType(TrustStoreOutput{})
}
