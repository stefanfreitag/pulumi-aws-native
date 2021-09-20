// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iot

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates an authorizer.
type Authorizer struct {
	pulumi.CustomResourceState

	Arn                    pulumi.StringOutput       `pulumi:"arn"`
	AuthorizerFunctionArn  pulumi.StringOutput       `pulumi:"authorizerFunctionArn"`
	AuthorizerName         pulumi.StringPtrOutput    `pulumi:"authorizerName"`
	SigningDisabled        pulumi.BoolPtrOutput      `pulumi:"signingDisabled"`
	Status                 AuthorizerStatusPtrOutput `pulumi:"status"`
	Tags                   AuthorizerTagArrayOutput  `pulumi:"tags"`
	TokenKeyName           pulumi.StringPtrOutput    `pulumi:"tokenKeyName"`
	TokenSigningPublicKeys pulumi.AnyOutput          `pulumi:"tokenSigningPublicKeys"`
}

// NewAuthorizer registers a new resource with the given unique name, arguments, and options.
func NewAuthorizer(ctx *pulumi.Context,
	name string, args *AuthorizerArgs, opts ...pulumi.ResourceOption) (*Authorizer, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AuthorizerFunctionArn == nil {
		return nil, errors.New("invalid value for required argument 'AuthorizerFunctionArn'")
	}
	var resource Authorizer
	err := ctx.RegisterResource("aws-native:iot:Authorizer", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAuthorizer gets an existing Authorizer resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAuthorizer(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AuthorizerState, opts ...pulumi.ResourceOption) (*Authorizer, error) {
	var resource Authorizer
	err := ctx.ReadResource("aws-native:iot:Authorizer", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Authorizer resources.
type authorizerState struct {
}

type AuthorizerState struct {
}

func (AuthorizerState) ElementType() reflect.Type {
	return reflect.TypeOf((*authorizerState)(nil)).Elem()
}

type authorizerArgs struct {
	AuthorizerFunctionArn  string            `pulumi:"authorizerFunctionArn"`
	AuthorizerName         *string           `pulumi:"authorizerName"`
	SigningDisabled        *bool             `pulumi:"signingDisabled"`
	Status                 *AuthorizerStatus `pulumi:"status"`
	Tags                   []AuthorizerTag   `pulumi:"tags"`
	TokenKeyName           *string           `pulumi:"tokenKeyName"`
	TokenSigningPublicKeys interface{}       `pulumi:"tokenSigningPublicKeys"`
}

// The set of arguments for constructing a Authorizer resource.
type AuthorizerArgs struct {
	AuthorizerFunctionArn  pulumi.StringInput
	AuthorizerName         pulumi.StringPtrInput
	SigningDisabled        pulumi.BoolPtrInput
	Status                 AuthorizerStatusPtrInput
	Tags                   AuthorizerTagArrayInput
	TokenKeyName           pulumi.StringPtrInput
	TokenSigningPublicKeys pulumi.Input
}

func (AuthorizerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*authorizerArgs)(nil)).Elem()
}

type AuthorizerInput interface {
	pulumi.Input

	ToAuthorizerOutput() AuthorizerOutput
	ToAuthorizerOutputWithContext(ctx context.Context) AuthorizerOutput
}

func (*Authorizer) ElementType() reflect.Type {
	return reflect.TypeOf((*Authorizer)(nil))
}

func (i *Authorizer) ToAuthorizerOutput() AuthorizerOutput {
	return i.ToAuthorizerOutputWithContext(context.Background())
}

func (i *Authorizer) ToAuthorizerOutputWithContext(ctx context.Context) AuthorizerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AuthorizerOutput)
}

type AuthorizerOutput struct{ *pulumi.OutputState }

func (AuthorizerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Authorizer)(nil))
}

func (o AuthorizerOutput) ToAuthorizerOutput() AuthorizerOutput {
	return o
}

func (o AuthorizerOutput) ToAuthorizerOutputWithContext(ctx context.Context) AuthorizerOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(AuthorizerOutput{})
}
