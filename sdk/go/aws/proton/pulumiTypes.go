// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package proton

import (
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
)

var _ = internal.GetEnvOrDefault

// <p>A description of a resource tag.</p>
type EnvironmentAccountConnectionTag struct {
	// <p>The key of the resource tag.</p>
	Key string `pulumi:"key"`
	// <p>The value of the resource tag.</p>
	Value string `pulumi:"value"`
}

// <p>A description of a resource tag.</p>
type EnvironmentTemplateTag struct {
	// <p>The key of the resource tag.</p>
	Key string `pulumi:"key"`
	// <p>The value of the resource tag.</p>
	Value string `pulumi:"value"`
}

// <p>A description of a resource tag.</p>
type ServiceTemplateTag struct {
	// <p>The key of the resource tag.</p>
	Key string `pulumi:"key"`
	// <p>The value of the resource tag.</p>
	Value string `pulumi:"value"`
}

func init() {
}
