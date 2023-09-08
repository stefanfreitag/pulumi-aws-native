// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package transfer

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Transfer::User
func LookupUser(ctx *pulumi.Context, args *LookupUserArgs, opts ...pulumi.InvokeOption) (*LookupUserResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupUserResult
	err := ctx.Invoke("aws-native:transfer:getUser", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupUserArgs struct {
	Id string `pulumi:"id"`
}

type LookupUserResult struct {
	Arn                   *string                     `pulumi:"arn"`
	HomeDirectory         *string                     `pulumi:"homeDirectory"`
	HomeDirectoryMappings []UserHomeDirectoryMapEntry `pulumi:"homeDirectoryMappings"`
	HomeDirectoryType     *string                     `pulumi:"homeDirectoryType"`
	Id                    *string                     `pulumi:"id"`
	Policy                *string                     `pulumi:"policy"`
	PosixProfile          *UserPosixProfile           `pulumi:"posixProfile"`
	Role                  *string                     `pulumi:"role"`
	SshPublicKeys         []UserSshPublicKey          `pulumi:"sshPublicKeys"`
	Tags                  []UserTag                   `pulumi:"tags"`
}

func LookupUserOutput(ctx *pulumi.Context, args LookupUserOutputArgs, opts ...pulumi.InvokeOption) LookupUserResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupUserResult, error) {
			args := v.(LookupUserArgs)
			r, err := LookupUser(ctx, &args, opts...)
			var s LookupUserResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupUserResultOutput)
}

type LookupUserOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupUserOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupUserArgs)(nil)).Elem()
}

type LookupUserResultOutput struct{ *pulumi.OutputState }

func (LookupUserResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupUserResult)(nil)).Elem()
}

func (o LookupUserResultOutput) ToLookupUserResultOutput() LookupUserResultOutput {
	return o
}

func (o LookupUserResultOutput) ToLookupUserResultOutputWithContext(ctx context.Context) LookupUserResultOutput {
	return o
}

func (o LookupUserResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupUserResult] {
	return pulumix.Output[LookupUserResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupUserResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupUserResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupUserResultOutput) HomeDirectory() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupUserResult) *string { return v.HomeDirectory }).(pulumi.StringPtrOutput)
}

func (o LookupUserResultOutput) HomeDirectoryMappings() UserHomeDirectoryMapEntryArrayOutput {
	return o.ApplyT(func(v LookupUserResult) []UserHomeDirectoryMapEntry { return v.HomeDirectoryMappings }).(UserHomeDirectoryMapEntryArrayOutput)
}

func (o LookupUserResultOutput) HomeDirectoryType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupUserResult) *string { return v.HomeDirectoryType }).(pulumi.StringPtrOutput)
}

func (o LookupUserResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupUserResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupUserResultOutput) Policy() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupUserResult) *string { return v.Policy }).(pulumi.StringPtrOutput)
}

func (o LookupUserResultOutput) PosixProfile() UserPosixProfilePtrOutput {
	return o.ApplyT(func(v LookupUserResult) *UserPosixProfile { return v.PosixProfile }).(UserPosixProfilePtrOutput)
}

func (o LookupUserResultOutput) Role() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupUserResult) *string { return v.Role }).(pulumi.StringPtrOutput)
}

func (o LookupUserResultOutput) SshPublicKeys() UserSshPublicKeyArrayOutput {
	return o.ApplyT(func(v LookupUserResult) []UserSshPublicKey { return v.SshPublicKeys }).(UserSshPublicKeyArrayOutput)
}

func (o LookupUserResultOutput) Tags() UserTagArrayOutput {
	return o.ApplyT(func(v LookupUserResult) []UserTag { return v.Tags }).(UserTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupUserResultOutput{})
}
