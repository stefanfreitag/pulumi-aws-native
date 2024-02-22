// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package voiceid

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::VoiceID::Domain resource specifies an Amazon VoiceID Domain.
type Domain struct {
	pulumi.CustomResourceState

	Description                       pulumi.StringPtrOutput                        `pulumi:"description"`
	DomainId                          pulumi.StringOutput                           `pulumi:"domainId"`
	Name                              pulumi.StringOutput                           `pulumi:"name"`
	ServerSideEncryptionConfiguration DomainServerSideEncryptionConfigurationOutput `pulumi:"serverSideEncryptionConfiguration"`
	Tags                              aws.TagArrayOutput                            `pulumi:"tags"`
}

// NewDomain registers a new resource with the given unique name, arguments, and options.
func NewDomain(ctx *pulumi.Context,
	name string, args *DomainArgs, opts ...pulumi.ResourceOption) (*Domain, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ServerSideEncryptionConfiguration == nil {
		return nil, errors.New("invalid value for required argument 'ServerSideEncryptionConfiguration'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Domain
	err := ctx.RegisterResource("aws-native:voiceid:Domain", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDomain gets an existing Domain resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDomain(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DomainState, opts ...pulumi.ResourceOption) (*Domain, error) {
	var resource Domain
	err := ctx.ReadResource("aws-native:voiceid:Domain", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Domain resources.
type domainState struct {
}

type DomainState struct {
}

func (DomainState) ElementType() reflect.Type {
	return reflect.TypeOf((*domainState)(nil)).Elem()
}

type domainArgs struct {
	Description                       *string                                 `pulumi:"description"`
	Name                              *string                                 `pulumi:"name"`
	ServerSideEncryptionConfiguration DomainServerSideEncryptionConfiguration `pulumi:"serverSideEncryptionConfiguration"`
	Tags                              []aws.Tag                               `pulumi:"tags"`
}

// The set of arguments for constructing a Domain resource.
type DomainArgs struct {
	Description                       pulumi.StringPtrInput
	Name                              pulumi.StringPtrInput
	ServerSideEncryptionConfiguration DomainServerSideEncryptionConfigurationInput
	Tags                              aws.TagArrayInput
}

func (DomainArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*domainArgs)(nil)).Elem()
}

type DomainInput interface {
	pulumi.Input

	ToDomainOutput() DomainOutput
	ToDomainOutputWithContext(ctx context.Context) DomainOutput
}

func (*Domain) ElementType() reflect.Type {
	return reflect.TypeOf((**Domain)(nil)).Elem()
}

func (i *Domain) ToDomainOutput() DomainOutput {
	return i.ToDomainOutputWithContext(context.Background())
}

func (i *Domain) ToDomainOutputWithContext(ctx context.Context) DomainOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainOutput)
}

type DomainOutput struct{ *pulumi.OutputState }

func (DomainOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Domain)(nil)).Elem()
}

func (o DomainOutput) ToDomainOutput() DomainOutput {
	return o
}

func (o DomainOutput) ToDomainOutputWithContext(ctx context.Context) DomainOutput {
	return o
}

func (o DomainOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o DomainOutput) DomainId() pulumi.StringOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringOutput { return v.DomainId }).(pulumi.StringOutput)
}

func (o DomainOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o DomainOutput) ServerSideEncryptionConfiguration() DomainServerSideEncryptionConfigurationOutput {
	return o.ApplyT(func(v *Domain) DomainServerSideEncryptionConfigurationOutput {
		return v.ServerSideEncryptionConfiguration
	}).(DomainServerSideEncryptionConfigurationOutput)
}

func (o DomainOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *Domain) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DomainInput)(nil)).Elem(), &Domain{})
	pulumi.RegisterOutputType(DomainOutput{})
}
