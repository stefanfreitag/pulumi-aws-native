// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appsync

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::AppSync::GraphQLApi
//
// Deprecated: GraphQLApi is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type GraphQLApi struct {
	pulumi.CustomResourceState

	AdditionalAuthenticationProviders GraphQLApiAdditionalAuthenticationProvidersPtrOutput `pulumi:"additionalAuthenticationProviders"`
	ApiId                             pulumi.StringOutput                                  `pulumi:"apiId"`
	Arn                               pulumi.StringOutput                                  `pulumi:"arn"`
	AuthenticationType                pulumi.StringOutput                                  `pulumi:"authenticationType"`
	GraphQLUrl                        pulumi.StringOutput                                  `pulumi:"graphQLUrl"`
	LambdaAuthorizerConfig            GraphQLApiLambdaAuthorizerConfigPtrOutput            `pulumi:"lambdaAuthorizerConfig"`
	LogConfig                         GraphQLApiLogConfigPtrOutput                         `pulumi:"logConfig"`
	Name                              pulumi.StringOutput                                  `pulumi:"name"`
	OpenIDConnectConfig               GraphQLApiOpenIDConnectConfigPtrOutput               `pulumi:"openIDConnectConfig"`
	Tags                              GraphQLApiTagsPtrOutput                              `pulumi:"tags"`
	UserPoolConfig                    GraphQLApiUserPoolConfigPtrOutput                    `pulumi:"userPoolConfig"`
	XrayEnabled                       pulumi.BoolPtrOutput                                 `pulumi:"xrayEnabled"`
}

// NewGraphQLApi registers a new resource with the given unique name, arguments, and options.
func NewGraphQLApi(ctx *pulumi.Context,
	name string, args *GraphQLApiArgs, opts ...pulumi.ResourceOption) (*GraphQLApi, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AuthenticationType == nil {
		return nil, errors.New("invalid value for required argument 'AuthenticationType'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource GraphQLApi
	err := ctx.RegisterResource("aws-native:appsync:GraphQLApi", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGraphQLApi gets an existing GraphQLApi resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGraphQLApi(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GraphQLApiState, opts ...pulumi.ResourceOption) (*GraphQLApi, error) {
	var resource GraphQLApi
	err := ctx.ReadResource("aws-native:appsync:GraphQLApi", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GraphQLApi resources.
type graphQLApiState struct {
}

type GraphQLApiState struct {
}

func (GraphQLApiState) ElementType() reflect.Type {
	return reflect.TypeOf((*graphQLApiState)(nil)).Elem()
}

type graphQLApiArgs struct {
	AdditionalAuthenticationProviders *GraphQLApiAdditionalAuthenticationProviders `pulumi:"additionalAuthenticationProviders"`
	AuthenticationType                string                                       `pulumi:"authenticationType"`
	LambdaAuthorizerConfig            *GraphQLApiLambdaAuthorizerConfig            `pulumi:"lambdaAuthorizerConfig"`
	LogConfig                         *GraphQLApiLogConfig                         `pulumi:"logConfig"`
	Name                              string                                       `pulumi:"name"`
	OpenIDConnectConfig               *GraphQLApiOpenIDConnectConfig               `pulumi:"openIDConnectConfig"`
	Tags                              *GraphQLApiTags                              `pulumi:"tags"`
	UserPoolConfig                    *GraphQLApiUserPoolConfig                    `pulumi:"userPoolConfig"`
	XrayEnabled                       *bool                                        `pulumi:"xrayEnabled"`
}

// The set of arguments for constructing a GraphQLApi resource.
type GraphQLApiArgs struct {
	AdditionalAuthenticationProviders GraphQLApiAdditionalAuthenticationProvidersPtrInput
	AuthenticationType                pulumi.StringInput
	LambdaAuthorizerConfig            GraphQLApiLambdaAuthorizerConfigPtrInput
	LogConfig                         GraphQLApiLogConfigPtrInput
	Name                              pulumi.StringInput
	OpenIDConnectConfig               GraphQLApiOpenIDConnectConfigPtrInput
	Tags                              GraphQLApiTagsPtrInput
	UserPoolConfig                    GraphQLApiUserPoolConfigPtrInput
	XrayEnabled                       pulumi.BoolPtrInput
}

func (GraphQLApiArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*graphQLApiArgs)(nil)).Elem()
}

type GraphQLApiInput interface {
	pulumi.Input

	ToGraphQLApiOutput() GraphQLApiOutput
	ToGraphQLApiOutputWithContext(ctx context.Context) GraphQLApiOutput
}

func (*GraphQLApi) ElementType() reflect.Type {
	return reflect.TypeOf((*GraphQLApi)(nil))
}

func (i *GraphQLApi) ToGraphQLApiOutput() GraphQLApiOutput {
	return i.ToGraphQLApiOutputWithContext(context.Background())
}

func (i *GraphQLApi) ToGraphQLApiOutputWithContext(ctx context.Context) GraphQLApiOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GraphQLApiOutput)
}

type GraphQLApiOutput struct{ *pulumi.OutputState }

func (GraphQLApiOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GraphQLApi)(nil))
}

func (o GraphQLApiOutput) ToGraphQLApiOutput() GraphQLApiOutput {
	return o
}

func (o GraphQLApiOutput) ToGraphQLApiOutputWithContext(ctx context.Context) GraphQLApiOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(GraphQLApiOutput{})
}
