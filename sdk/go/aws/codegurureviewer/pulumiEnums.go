// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package codegurureviewer

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The type of repository to be associated.
type RepositoryAssociationType string

const (
	RepositoryAssociationTypeCodeCommit             = RepositoryAssociationType("CodeCommit")
	RepositoryAssociationTypeBitbucket              = RepositoryAssociationType("Bitbucket")
	RepositoryAssociationTypeGitHubEnterpriseServer = RepositoryAssociationType("GitHubEnterpriseServer")
	RepositoryAssociationTypeS3Bucket               = RepositoryAssociationType("S3Bucket")
)

func (RepositoryAssociationType) ElementType() reflect.Type {
	return reflect.TypeOf((*RepositoryAssociationType)(nil)).Elem()
}

func (e RepositoryAssociationType) ToRepositoryAssociationTypeOutput() RepositoryAssociationTypeOutput {
	return pulumi.ToOutput(e).(RepositoryAssociationTypeOutput)
}

func (e RepositoryAssociationType) ToRepositoryAssociationTypeOutputWithContext(ctx context.Context) RepositoryAssociationTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(RepositoryAssociationTypeOutput)
}

func (e RepositoryAssociationType) ToRepositoryAssociationTypePtrOutput() RepositoryAssociationTypePtrOutput {
	return e.ToRepositoryAssociationTypePtrOutputWithContext(context.Background())
}

func (e RepositoryAssociationType) ToRepositoryAssociationTypePtrOutputWithContext(ctx context.Context) RepositoryAssociationTypePtrOutput {
	return RepositoryAssociationType(e).ToRepositoryAssociationTypeOutputWithContext(ctx).ToRepositoryAssociationTypePtrOutputWithContext(ctx)
}

func (e RepositoryAssociationType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e RepositoryAssociationType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e RepositoryAssociationType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e RepositoryAssociationType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type RepositoryAssociationTypeOutput struct{ *pulumi.OutputState }

func (RepositoryAssociationTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*RepositoryAssociationType)(nil)).Elem()
}

func (o RepositoryAssociationTypeOutput) ToRepositoryAssociationTypeOutput() RepositoryAssociationTypeOutput {
	return o
}

func (o RepositoryAssociationTypeOutput) ToRepositoryAssociationTypeOutputWithContext(ctx context.Context) RepositoryAssociationTypeOutput {
	return o
}

func (o RepositoryAssociationTypeOutput) ToRepositoryAssociationTypePtrOutput() RepositoryAssociationTypePtrOutput {
	return o.ToRepositoryAssociationTypePtrOutputWithContext(context.Background())
}

func (o RepositoryAssociationTypeOutput) ToRepositoryAssociationTypePtrOutputWithContext(ctx context.Context) RepositoryAssociationTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v RepositoryAssociationType) *RepositoryAssociationType {
		return &v
	}).(RepositoryAssociationTypePtrOutput)
}

func (o RepositoryAssociationTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o RepositoryAssociationTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e RepositoryAssociationType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o RepositoryAssociationTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o RepositoryAssociationTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e RepositoryAssociationType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type RepositoryAssociationTypePtrOutput struct{ *pulumi.OutputState }

func (RepositoryAssociationTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RepositoryAssociationType)(nil)).Elem()
}

func (o RepositoryAssociationTypePtrOutput) ToRepositoryAssociationTypePtrOutput() RepositoryAssociationTypePtrOutput {
	return o
}

func (o RepositoryAssociationTypePtrOutput) ToRepositoryAssociationTypePtrOutputWithContext(ctx context.Context) RepositoryAssociationTypePtrOutput {
	return o
}

func (o RepositoryAssociationTypePtrOutput) Elem() RepositoryAssociationTypeOutput {
	return o.ApplyT(func(v *RepositoryAssociationType) RepositoryAssociationType {
		if v != nil {
			return *v
		}
		var ret RepositoryAssociationType
		return ret
	}).(RepositoryAssociationTypeOutput)
}

func (o RepositoryAssociationTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o RepositoryAssociationTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *RepositoryAssociationType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// RepositoryAssociationTypeInput is an input type that accepts RepositoryAssociationTypeArgs and RepositoryAssociationTypeOutput values.
// You can construct a concrete instance of `RepositoryAssociationTypeInput` via:
//
//          RepositoryAssociationTypeArgs{...}
type RepositoryAssociationTypeInput interface {
	pulumi.Input

	ToRepositoryAssociationTypeOutput() RepositoryAssociationTypeOutput
	ToRepositoryAssociationTypeOutputWithContext(context.Context) RepositoryAssociationTypeOutput
}

var repositoryAssociationTypePtrType = reflect.TypeOf((**RepositoryAssociationType)(nil)).Elem()

type RepositoryAssociationTypePtrInput interface {
	pulumi.Input

	ToRepositoryAssociationTypePtrOutput() RepositoryAssociationTypePtrOutput
	ToRepositoryAssociationTypePtrOutputWithContext(context.Context) RepositoryAssociationTypePtrOutput
}

type repositoryAssociationTypePtr string

func RepositoryAssociationTypePtr(v string) RepositoryAssociationTypePtrInput {
	return (*repositoryAssociationTypePtr)(&v)
}

func (*repositoryAssociationTypePtr) ElementType() reflect.Type {
	return repositoryAssociationTypePtrType
}

func (in *repositoryAssociationTypePtr) ToRepositoryAssociationTypePtrOutput() RepositoryAssociationTypePtrOutput {
	return pulumi.ToOutput(in).(RepositoryAssociationTypePtrOutput)
}

func (in *repositoryAssociationTypePtr) ToRepositoryAssociationTypePtrOutputWithContext(ctx context.Context) RepositoryAssociationTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(RepositoryAssociationTypePtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RepositoryAssociationTypeInput)(nil)).Elem(), RepositoryAssociationType("CodeCommit"))
	pulumi.RegisterInputType(reflect.TypeOf((*RepositoryAssociationTypePtrInput)(nil)).Elem(), RepositoryAssociationType("CodeCommit"))
	pulumi.RegisterOutputType(RepositoryAssociationTypeOutput{})
	pulumi.RegisterOutputType(RepositoryAssociationTypePtrOutput{})
}
