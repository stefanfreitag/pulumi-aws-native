// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lex.Outputs
{

    /// <summary>
    /// Settings that specify the dialog code hook that is called by Amazon Lex between eliciting slot values.
    /// </summary>
    [OutputType]
    public sealed class BotElicitationCodeHookInvocationSetting
    {
        /// <summary>
        /// Indicates whether a Lambda function should be invoked for the dialog.
        /// </summary>
        public readonly bool EnableCodeHookInvocation;
        /// <summary>
        /// A label that indicates the dialog step from which the dialog code hook is happening.
        /// </summary>
        public readonly string? InvocationLabel;

        [OutputConstructor]
        private BotElicitationCodeHookInvocationSetting(
            bool enableCodeHookInvocation,

            string? invocationLabel)
        {
            EnableCodeHookInvocation = enableCodeHookInvocation;
            InvocationLabel = invocationLabel;
        }
    }
}
