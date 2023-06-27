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
    /// Configuration setting for a response sent to the user before Amazon Lex starts eliciting slots.
    /// </summary>
    [OutputType]
    public sealed class BotInitialResponseSetting
    {
        /// <summary>
        /// Settings that specify the dialog code hook that is called by Amazon Lex at a step of the conversation.
        /// </summary>
        public readonly Outputs.BotDialogCodeHookInvocationSetting? CodeHook;
        /// <summary>
        /// Provides a list of conditional branches. Branches are evaluated in the order that they are entered in the list. The first branch with a condition that evaluates to true is executed. The last branch in the list is the default branch. The default branch should not have any condition expression. The default branch is executed if no other branch has a matching condition.
        /// </summary>
        public readonly Outputs.BotConditionalSpecification? Conditional;
        /// <summary>
        /// Specifies a list of message groups that Amazon Lex uses to respond the user input.
        /// </summary>
        public readonly Outputs.BotResponseSpecification? InitialResponse;
        /// <summary>
        /// The next step in the conversation.
        /// </summary>
        public readonly Outputs.BotDialogState? NextStep;

        [OutputConstructor]
        private BotInitialResponseSetting(
            Outputs.BotDialogCodeHookInvocationSetting? codeHook,

            Outputs.BotConditionalSpecification? conditional,

            Outputs.BotResponseSpecification? initialResponse,

            Outputs.BotDialogState? nextStep)
        {
            CodeHook = codeHook;
            Conditional = conditional;
            InitialResponse = initialResponse;
            NextStep = nextStep;
        }
    }
}
