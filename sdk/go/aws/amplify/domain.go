// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package amplify

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::Amplify::Domain resource allows you to connect a custom domain to your app.
type Domain struct {
	pulumi.CustomResourceState

	AppId                         pulumi.StringOutput               `pulumi:"appId"`
	Arn                           pulumi.StringOutput               `pulumi:"arn"`
	AutoSubDomainCreationPatterns pulumi.StringArrayOutput          `pulumi:"autoSubDomainCreationPatterns"`
	AutoSubDomainIAMRole          pulumi.StringPtrOutput            `pulumi:"autoSubDomainIAMRole"`
	CertificateRecord             pulumi.StringOutput               `pulumi:"certificateRecord"`
	DomainName                    pulumi.StringOutput               `pulumi:"domainName"`
	DomainStatus                  pulumi.StringOutput               `pulumi:"domainStatus"`
	EnableAutoSubDomain           pulumi.BoolPtrOutput              `pulumi:"enableAutoSubDomain"`
	StatusReason                  pulumi.StringOutput               `pulumi:"statusReason"`
	SubDomainSettings             DomainSubDomainSettingArrayOutput `pulumi:"subDomainSettings"`
}

// NewDomain registers a new resource with the given unique name, arguments, and options.
func NewDomain(ctx *pulumi.Context,
	name string, args *DomainArgs, opts ...pulumi.ResourceOption) (*Domain, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AppId == nil {
		return nil, errors.New("invalid value for required argument 'AppId'")
	}
	if args.DomainName == nil {
		return nil, errors.New("invalid value for required argument 'DomainName'")
	}
	if args.SubDomainSettings == nil {
		return nil, errors.New("invalid value for required argument 'SubDomainSettings'")
	}
	var resource Domain
	err := ctx.RegisterResource("aws-native:amplify:Domain", name, args, &resource, opts...)
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
	err := ctx.ReadResource("aws-native:amplify:Domain", name, id, state, &resource, opts...)
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
	AppId                         string                   `pulumi:"appId"`
	AutoSubDomainCreationPatterns []string                 `pulumi:"autoSubDomainCreationPatterns"`
	AutoSubDomainIAMRole          *string                  `pulumi:"autoSubDomainIAMRole"`
	DomainName                    string                   `pulumi:"domainName"`
	EnableAutoSubDomain           *bool                    `pulumi:"enableAutoSubDomain"`
	SubDomainSettings             []DomainSubDomainSetting `pulumi:"subDomainSettings"`
}

// The set of arguments for constructing a Domain resource.
type DomainArgs struct {
	AppId                         pulumi.StringInput
	AutoSubDomainCreationPatterns pulumi.StringArrayInput
	AutoSubDomainIAMRole          pulumi.StringPtrInput
	DomainName                    pulumi.StringInput
	EnableAutoSubDomain           pulumi.BoolPtrInput
	SubDomainSettings             DomainSubDomainSettingArrayInput
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
	return reflect.TypeOf((*Domain)(nil))
}

func (i *Domain) ToDomainOutput() DomainOutput {
	return i.ToDomainOutputWithContext(context.Background())
}

func (i *Domain) ToDomainOutputWithContext(ctx context.Context) DomainOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainOutput)
}

type DomainOutput struct{ *pulumi.OutputState }

func (DomainOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Domain)(nil))
}

func (o DomainOutput) ToDomainOutput() DomainOutput {
	return o
}

func (o DomainOutput) ToDomainOutputWithContext(ctx context.Context) DomainOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(DomainOutput{})
}
