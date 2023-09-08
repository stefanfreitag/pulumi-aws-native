// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appsync

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::AppSync::DomainName
type DomainName struct {
	pulumi.CustomResourceState

	AppSyncDomainName pulumi.StringOutput    `pulumi:"appSyncDomainName"`
	CertificateArn    pulumi.StringOutput    `pulumi:"certificateArn"`
	Description       pulumi.StringPtrOutput `pulumi:"description"`
	DomainName        pulumi.StringOutput    `pulumi:"domainName"`
	HostedZoneId      pulumi.StringOutput    `pulumi:"hostedZoneId"`
}

// NewDomainName registers a new resource with the given unique name, arguments, and options.
func NewDomainName(ctx *pulumi.Context,
	name string, args *DomainNameArgs, opts ...pulumi.ResourceOption) (*DomainName, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CertificateArn == nil {
		return nil, errors.New("invalid value for required argument 'CertificateArn'")
	}
	if args.DomainName == nil {
		return nil, errors.New("invalid value for required argument 'DomainName'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"certificateArn",
		"domainName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DomainName
	err := ctx.RegisterResource("aws-native:appsync:DomainName", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDomainName gets an existing DomainName resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDomainName(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DomainNameState, opts ...pulumi.ResourceOption) (*DomainName, error) {
	var resource DomainName
	err := ctx.ReadResource("aws-native:appsync:DomainName", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DomainName resources.
type domainNameState struct {
}

type DomainNameState struct {
}

func (DomainNameState) ElementType() reflect.Type {
	return reflect.TypeOf((*domainNameState)(nil)).Elem()
}

type domainNameArgs struct {
	CertificateArn string  `pulumi:"certificateArn"`
	Description    *string `pulumi:"description"`
	DomainName     string  `pulumi:"domainName"`
}

// The set of arguments for constructing a DomainName resource.
type DomainNameArgs struct {
	CertificateArn pulumi.StringInput
	Description    pulumi.StringPtrInput
	DomainName     pulumi.StringInput
}

func (DomainNameArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*domainNameArgs)(nil)).Elem()
}

type DomainNameInput interface {
	pulumi.Input

	ToDomainNameOutput() DomainNameOutput
	ToDomainNameOutputWithContext(ctx context.Context) DomainNameOutput
}

func (*DomainName) ElementType() reflect.Type {
	return reflect.TypeOf((**DomainName)(nil)).Elem()
}

func (i *DomainName) ToDomainNameOutput() DomainNameOutput {
	return i.ToDomainNameOutputWithContext(context.Background())
}

func (i *DomainName) ToDomainNameOutputWithContext(ctx context.Context) DomainNameOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainNameOutput)
}

func (i *DomainName) ToOutput(ctx context.Context) pulumix.Output[*DomainName] {
	return pulumix.Output[*DomainName]{
		OutputState: i.ToDomainNameOutputWithContext(ctx).OutputState,
	}
}

type DomainNameOutput struct{ *pulumi.OutputState }

func (DomainNameOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DomainName)(nil)).Elem()
}

func (o DomainNameOutput) ToDomainNameOutput() DomainNameOutput {
	return o
}

func (o DomainNameOutput) ToDomainNameOutputWithContext(ctx context.Context) DomainNameOutput {
	return o
}

func (o DomainNameOutput) ToOutput(ctx context.Context) pulumix.Output[*DomainName] {
	return pulumix.Output[*DomainName]{
		OutputState: o.OutputState,
	}
}

func (o DomainNameOutput) AppSyncDomainName() pulumi.StringOutput {
	return o.ApplyT(func(v *DomainName) pulumi.StringOutput { return v.AppSyncDomainName }).(pulumi.StringOutput)
}

func (o DomainNameOutput) CertificateArn() pulumi.StringOutput {
	return o.ApplyT(func(v *DomainName) pulumi.StringOutput { return v.CertificateArn }).(pulumi.StringOutput)
}

func (o DomainNameOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DomainName) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o DomainNameOutput) DomainName() pulumi.StringOutput {
	return o.ApplyT(func(v *DomainName) pulumi.StringOutput { return v.DomainName }).(pulumi.StringOutput)
}

func (o DomainNameOutput) HostedZoneId() pulumi.StringOutput {
	return o.ApplyT(func(v *DomainName) pulumi.StringOutput { return v.HostedZoneId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DomainNameInput)(nil)).Elem(), &DomainName{})
	pulumi.RegisterOutputType(DomainNameOutput{})
}
