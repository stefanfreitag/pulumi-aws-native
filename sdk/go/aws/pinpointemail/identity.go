// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package pinpointemail

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::PinpointEmail::Identity
//
// Deprecated: Identity is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Identity struct {
	pulumi.CustomResourceState

	DkimSigningEnabled        pulumi.BoolPtrOutput                `pulumi:"dkimSigningEnabled"`
	FeedbackForwardingEnabled pulumi.BoolPtrOutput                `pulumi:"feedbackForwardingEnabled"`
	IdentityDNSRecordName1    pulumi.StringOutput                 `pulumi:"identityDNSRecordName1"`
	IdentityDNSRecordName2    pulumi.StringOutput                 `pulumi:"identityDNSRecordName2"`
	IdentityDNSRecordName3    pulumi.StringOutput                 `pulumi:"identityDNSRecordName3"`
	IdentityDNSRecordValue1   pulumi.StringOutput                 `pulumi:"identityDNSRecordValue1"`
	IdentityDNSRecordValue2   pulumi.StringOutput                 `pulumi:"identityDNSRecordValue2"`
	IdentityDNSRecordValue3   pulumi.StringOutput                 `pulumi:"identityDNSRecordValue3"`
	MailFromAttributes        IdentityMailFromAttributesPtrOutput `pulumi:"mailFromAttributes"`
	Name                      pulumi.StringOutput                 `pulumi:"name"`
	Tags                      IdentityTagsArrayOutput             `pulumi:"tags"`
}

// NewIdentity registers a new resource with the given unique name, arguments, and options.
func NewIdentity(ctx *pulumi.Context,
	name string, args *IdentityArgs, opts ...pulumi.ResourceOption) (*Identity, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource Identity
	err := ctx.RegisterResource("aws-native:pinpointemail:Identity", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIdentity gets an existing Identity resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIdentity(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IdentityState, opts ...pulumi.ResourceOption) (*Identity, error) {
	var resource Identity
	err := ctx.ReadResource("aws-native:pinpointemail:Identity", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Identity resources.
type identityState struct {
}

type IdentityState struct {
}

func (IdentityState) ElementType() reflect.Type {
	return reflect.TypeOf((*identityState)(nil)).Elem()
}

type identityArgs struct {
	DkimSigningEnabled        *bool                       `pulumi:"dkimSigningEnabled"`
	FeedbackForwardingEnabled *bool                       `pulumi:"feedbackForwardingEnabled"`
	MailFromAttributes        *IdentityMailFromAttributes `pulumi:"mailFromAttributes"`
	Name                      string                      `pulumi:"name"`
	Tags                      []IdentityTags              `pulumi:"tags"`
}

// The set of arguments for constructing a Identity resource.
type IdentityArgs struct {
	DkimSigningEnabled        pulumi.BoolPtrInput
	FeedbackForwardingEnabled pulumi.BoolPtrInput
	MailFromAttributes        IdentityMailFromAttributesPtrInput
	Name                      pulumi.StringInput
	Tags                      IdentityTagsArrayInput
}

func (IdentityArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*identityArgs)(nil)).Elem()
}

type IdentityInput interface {
	pulumi.Input

	ToIdentityOutput() IdentityOutput
	ToIdentityOutputWithContext(ctx context.Context) IdentityOutput
}

func (*Identity) ElementType() reflect.Type {
	return reflect.TypeOf((*Identity)(nil))
}

func (i *Identity) ToIdentityOutput() IdentityOutput {
	return i.ToIdentityOutputWithContext(context.Background())
}

func (i *Identity) ToIdentityOutputWithContext(ctx context.Context) IdentityOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IdentityOutput)
}

type IdentityOutput struct{ *pulumi.OutputState }

func (IdentityOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Identity)(nil))
}

func (o IdentityOutput) ToIdentityOutput() IdentityOutput {
	return o
}

func (o IdentityOutput) ToIdentityOutputWithContext(ctx context.Context) IdentityOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*IdentityInput)(nil)).Elem(), &Identity{})
	pulumi.RegisterOutputType(IdentityOutput{})
}
